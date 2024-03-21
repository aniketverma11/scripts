import pymongo
from faker import Faker

# Connect to MongoDB
connection_string = "mongodb+srv://username:password@host/"
client = pymongo.MongoClient(connection_string)
db = client["database_name"]
collection = db["object_name"]

# Create Faker instance
fake = Faker()

used_emails = set()

# Generate and insert 500 records
for _ in range(300):
    name = fake.name()
    email = name.replace(" ", ".").lower() + "@example.com"  # Create email based on name
    # Ensure email uniqueness
    while email in used_emails:
        name = fake.name()
        email = name.replace(" ", ".").lower() + "@example.com"
    used_emails.add(email)
    profile = {
        "profileViews": 0,
        "profilePictureApproved": fake.boolean(),
        "sharingApproved": fake.boolean(),
        "reputations": [],
        "interests": [],
        "hobbies": [],
        "questionList": [
            {"question": "Are you interested in a long-term relationship/marriage?", "answer": fake.random_element(["YES", "NO"])},
            {"question": "Have you ever traveled internationally?", "answer": fake.random_element(["YES", "NO"])},
            {"question": "Do you make over $75K a year?", "answer": fake.random_element(["YES", "NO"])},
            {"question": "Do you make your living from being an entrepreneur?", "answer": fake.random_element(["YES", "NO"])},
            {"question": "Do you have a Bachelor’s degree ?", "answer": fake.random_element(["YES", "NO"])},
        ],
        "aboutMe": fake.text(),
        "age": fake.random_int(min=18, max=60),
        "body": fake.random_element(["SLIM", "AVERAGE", "ATHLETIC", "CURVY"]),
        "drinking": fake.random_element(["NEVER", "OCCASIONALLY", "REGULARLY"]),
        "education": fake.random_element(["HIGH SCHOOL", "BACHELOR", "MASTERATE", "PHD"]),
        "ethnicity": fake.random_element(["CAUCASIAN", "AFRICAN", "ASIAN", "LATINO", "OTHER"]),
        "eyes": fake.random_element(["BLUE", "BROWN", "GREEN", "GREY"]),
        "gender": fake.random_element(["MALE", "FEMALE"]),
        "hair": fake.random_element(["BLACK", "BROWN", "BLONDE", "RED", "OTHER"]),
        "sexuality": fake.random_element(["STRAIGHT", "GAY", "BISEXUAL"]),
        "smoking": fake.random_element(["NEVER", "OCCASIONALLY", "REGULARLY"]),
        "verificationId": fake.file_name(),
        "preferences": {
            "ageMin": fake.random_int(min=18, max=40),
            "ageMax": fake.random_int(min=30, max=60),
            "interestedGender": fake.random_element(["MALE", "FEMALE", "BOTH"]),
            "sexuality": fake.random_element(["STRAIGHT", "GAY", "BISEXUAL", ""]),
            "ethnicity": fake.random_element(["CAUCASIAN", "AFRICAN", "ASIAN", "LATINO", "OTHER", ""]),
            "education": fake.random_element(["HIGH SCHOOL", "BACHELOR", "MASTERATE", "PHD", ""]),
        },
        "mainProfilePicture": fake.file_name(),
        "profilePictures": [fake.file_name()],
    }
    user = {
        "email": email,
        "signInType": "EMAIL",
        "subscriptionActive": fake.boolean(),
        "subscriptionVerifying": fake.boolean(),
        "isVerified": fake.boolean(),
        "isProfileVerified": fake.boolean(),
        "chargeBeCustomerId": fake.uuid4(),
        "idToken": None,
        "__v": 0,
        "profile": profile,
        "status": fake.random_element(["NON_BOARDED", "BOARDED"]),
        "password": fake.password(),
        "subscriptionType": fake.random_element(["MONTHLY", "YEARLY"]),
        "name": name,
    }
    collection.insert_one(user)
    print(_)

print("records inserted successfully.")
