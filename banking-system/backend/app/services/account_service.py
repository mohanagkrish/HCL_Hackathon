from app.repositories.account_repository import AccountRepository
from app.utils.helpers import generate_account_number
from fastapi import HTTPException, status

class AccountService:
    MIN_DEPOSIT = {
        "savings": 500,
        "current": 1000,
        "fd": 5000
    }

    @staticmethod
    def create_account(db, account_data):
        account_type = account_data.account_type.lower()

        if account_type not in AccountService.MIN_DEPOSIT:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid account type")

        min_amount = AccountService.MIN_DEPOSIT[account_type]
        if account_data.initial_deposit < min_amount:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Minimum deposit for {account_type} is ${min_amount}"
            )

        account_number = generate_account_number()
        existing = AccountRepository.get_account_by_number(db, account_number)
        while existing:
            account_number = generate_account_number()
            existing = AccountRepository.get_account_by_number(db, account_number)

        new_account = AccountRepository.create_account(
            db=db,
            account_number=account_number,
            account_type=account_type,
            initial_deposit=account_data.initial_deposit
        )

        return new_account
