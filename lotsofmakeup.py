from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Brand, Base, MackeupItem, User

engine = create_engine('sqlite:///mackeupitemtypewithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="nasser mustafa", email="12346@example.com",
             picture='https://images.pexels.com/photos/1662570/pexels-photo-1662570.jpeg')
session.add(User1)
session.commit()

# Menu for UrbanBurger
brand1 = Brand(user_id=1, name="mac")

session.add(brand1)
session.commit()

mackeup_item1 = MackeupItem(user_id=1, name="red eyeshadow", description="A highly pigmented powder that applies evenly and blends well.",
                            price="$7.50", type="Eyeshadow", brand=brand1)

session.add(mackeup_item1)
session.commit()

mackeup_item2 = MackeupItem(user_id=1, name="blue eyeshadow", description="A highly pigmented powder that applies evenly and blends well.",
                            price="$12.50", type="Eyeshadow", brand=brand1)

session.add(mackeup_item2)
session.commit()

mackeup_item3 = MackeupItem(user_id=1, name="brown eyeshadow", description="A highly pigmented powder that applies evenly and blends well.",
                            price="$12.50", type="Eyeshadow", brand=brand1)

session.add(mackeup_item3)
session.commit()

brand2 = Brand(user_id=1, name="sephora")

session.add(brand2)
session.commit()

mackeup_item4 = MackeupItem(user_id=1, name="red lipstick", description="A highly pigmented lipstick that applies evenly and blends well.",
                            price="$12.50", type="Eyeshadow", brand=brand2)

session.add(mackeup_item4)
session.commit()
print "added mackeup items!"
