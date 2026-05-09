import time


class RetryUtil:

    @staticmethod
    def retry_action(action, retries=3, delay=2):

        for attempt in range(retries):

            try:
                return action()

            except Exception as e:

                print(f"Retry {attempt + 1} failed: {e}")

                if attempt < retries - 1:
                    time.sleep(delay)

                else:
                    raise

                