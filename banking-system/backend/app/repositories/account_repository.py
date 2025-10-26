from sqlalchemy.orm import Session
from app.models.account_model import Account

class AccountRepository:
    @staticmethod
    def create_account(db: Session, account_number: str, account_type: str, initial_deposit: float):
        new_account = Account(
            account_number=account_number,
            account_type=account_type,
            initial_deposit=initial_deposit
        )
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return new_account

    @staticmethod
    def get_account_by_number(db: Session, account_number: str):
        return db.query(Account).filter(Account.account_number == account_number).first()
