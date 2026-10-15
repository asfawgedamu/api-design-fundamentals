# =========================================
#In this file, we are defining the service layer for the Order model. The service layer is responsible for handling the business logic of the application, such as creating new orders and retrieving existing orders. By separating the service layer from the data access layer (which interacts with the database), we can keep our code organized and maintainable. This also allows us to easily change the underlying data storage mechanism in the future without affecting the rest of the application.
#

from sqlalchemy.orm import Session

from app.models import DBOrder

def create_new_order(db: Session, order_data):

    new_order = DBOrder(**order_data.model_dump())

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

def get_all_orders(db: Session):

    return db.query(DBOrder).all()