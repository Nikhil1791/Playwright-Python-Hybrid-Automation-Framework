from faker import Faker
import random

fake = Faker()


class CommonUtil:

    @staticmethod
    def generate_random_email():
        return fake.email()

    @staticmethod
    def generate_random_name():
        return fake.name()

    @staticmethod
    def generate_random_number():
        return random.randint(1000, 9999)
    
    