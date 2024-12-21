#cashFlow.py

import datetime

class PaymentSystem:
    def __init__(self):
        self.accounts = {}  # 用戶帳戶資料，格式：{user_id: balance}
        self.transaction_history = []  # 交易記錄

    def create_account(self, user_id: str, initial_balance: float):
        """建立用戶帳戶並初始化餘額"""
        if user_id in self.accounts:
            raise ValueError("Account already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.accounts[user_id] = initial_balance

    def process_payment(self, user_id: str, amount: float) -> bool:
        """
        處理支付邏輯：
        - 檢查用戶是否存在
        - 確認餘額足夠
        - 扣款並記錄交易
        """
        if user_id not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        if self.accounts[user_id] < amount:
            return False  # 餘額不足

        # 扣款並記錄交易
        self.accounts[user_id] -= amount
        self.record_transaction(user_id, amount)
        return True

    def record_transaction(self, user_id: str, amount: float):
        """記錄交易歷史"""
        transaction = {
            "user_id": user_id,
            "amount": amount,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.transaction_history.append(transaction)

    def get_balance(self, user_id: str) -> float:
        """查詢用戶餘額"""
        if user_id not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[user_id]

    def get_transaction_history(self, user_id: str):
        """查詢用戶的交易記錄"""
        return [t for t in self.transaction_history if t["user_id"] == user_id]

# 實例化系統
system = PaymentSystem()

# 建立帳戶
system.create_account("Yun", 100.0)

# 支付操作
system.process_payment("Yun", 30.0)

# 查詢餘額
print(f"目前餘額：{system.get_balance('Yun')}")

# 查詢交易記錄
print("交易記錄：", system.get_transaction_history("Yun"))
