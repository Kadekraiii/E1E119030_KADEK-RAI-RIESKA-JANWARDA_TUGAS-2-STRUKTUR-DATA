class CreditCard:
  #A consumer credit card.
  
  def __init__(self, customer, bank, acnt, limit, balance=0):
    
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0
 
  def get_customer(self):
    """Kembalikan nama pelanggan."""
    return self._customer
    
  def get_bank(self):
    """Kembalikan nama bank."""
    return self._bank
 
  def get_account(self):
    """Kembalikan nomor identifikasi kartu (biasanya disimpan sebagai string)."""
    return self._account
 
  def get_limit(self):
    """Kembalikan batas kredit saat ini."""
    return self._limit
 
  def get_balance(self):
    """Kembalikan saldo saat ini."""
    return self._balance
 
  def charge(self, price):
      
    """Mengisi harga yang diberikan ke kartu, dengan asumsi batas kredit yang cukup.
    Kembalikan Benar jika tagihan diproses; Salah jika tuduhan ditolak.
    """
    if not isinstance(price, (int, float)):
        raise TypeError('harga harus numerik')
    if price + self._balance > self._limit:  
      return False                           
    else:
      self._balance += price
      return True
 
  def make_payment(self, amount):
    """Memproses pembayaran pelanggan yang mengurangi saldo.."""
    if not isinstance(amount, (int, float)):
        raise TypeError('amount must be numeric')
    self._balance -= amount
 
if __name__ == '__main__':
  wallet = []
  wallet.append(CreditCard('Kadek Rai', 'BRI',
                           '5391 0375 9387 5309', 2500) )
  wallet.append(CreditCard('Kadek Rai', 'BCA',
                           '3485 0399 3395 1954', 3500) )
  wallet.append(CreditCard('Kadek Rai', 'BTN',
                           '5391 0375 9387 5309', 5000) )
 
  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)
 
  for c in range(3):
    print('Customer =', wallet[c].get_customer())
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print('Balance =', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print('New balance =', wallet[c].get_balance())
    print()
