import cv2
import mediapipe as mp


class HandController:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(
                model_asset_path="hand_landmarker.task"
            ),
            running_mode=mp.tasks.vision.RunningMode.IMAGE,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.hand_detector = (
            mp.tasks.vision.HandLandmarker
            .create_from_options(options)
        )

        self.x = 0.5
        self.y = 0.5

        self.smooth_x = 0.5
        self.smooth_y = 0.5

        self.detected = False
        self.fingers = 0

    def get_control(self):
        success, frame = self.camera.read()

        if not success:
            return (
                self.x,
                self.y,
                False,
                self.fingers,
                None
            )

        # Mirror camera
        frame = cv2.flip(frame, 1)

        # BGR → RGB
        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.hand_detector.detect(mp_image)

        self.detected = False

        if result.hand_landmarks:

            points = result.hand_landmarks[0]

            self.detected = True

            # Palm center
            x = (
                points[0].x +
                points[5].x +
                points[9].x +
                points[13].x +
                points[17].x
            ) / 5

            y = (
                points[0].y +
                points[5].y +
                points[9].y +
                points[13].y +
                points[17].y
            ) / 5

            # Smooth movement
            self.smooth_x += (
                x - self.smooth_x
            ) * 0.25

            self.smooth_y += (
                y - self.smooth_y
            ) * 0.25

            self.x = self.smooth_x
            self.y = self.smooth_y

            self.fingers = self.count_fingers(points)

            # Draw hand
            h, w = frame.shape[:2]

            for connection in (
                mp.tasks.vision
                .HandLandmarksConnections
                .HAND_CONNECTIONS
            ):
                p1 = points[connection.start]
                p2 = points[connection.end]

                cv2.line(
                    frame,
                    (
                        int(p1.x * w),
                        int(p1.y * h)
                    ),
                    (
                        int(p2.x * w),
                        int(p2.y * h)
                    ),
                    (0, 255, 0),
                    2
                )

            # Draw landmarks
            for point in points:

                cv2.circle(
                    frame,
                    (
                        int(point.x * w),
                        int(point.y * h)
                    ),
                    4,
                    (0, 0, 255),
                    -1
                )

        return (
            self.x,
            self.y,
            self.detected,
            self.fingers,
            frame
        )

    def count_fingers(self, points):

        fingers = 0

        # Thumb
        if points[4].x < points[3].x:
            fingers += 1

        # Index
        if points[8].y < points[6].y:
            fingers += 1

        # Middle
        if points[12].y < points[10].y:
            fingers += 1

        # Ring
        if points[16].y < points[14].y:
            fingers += 1

        # Little
        if points[20].y < points[18].y:
            fingers += 1

        return fingers

    def release(self):
        self.camera.release()
        self.hand_detector.close()
        cv2.destroyAllWindows()