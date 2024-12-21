#test_cashFlow.py

from cashFlow import PaymentSystem

def test_cashFlow():
    # 實例化系統
    system = PaymentSystem()

    # 建立帳戶
    system.create_account("Yun", 100.0)

    # 驗證帳戶是否成功建立
    balance = system.get_balance("Yun")  # 查詢餘額
    assert balance == 100.0, f"預期餘額為 100.0，但實際為 {balance}"

    result = system.process_payment("Yun", 30.0)
    assert result == 70.0

    print("測試通過：帳戶成功建立且初始餘額正確。")
    