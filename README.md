How to Use the Project:

Clone the repository:
git clone https://github.com/yourusername/trading-system.git
cd trading-system

Install required packages:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser (for Django Admin):
python manage.py createsuperuser

Run the server:
python manage.py runserver

Access the Django Admin Panel:
http://127.0.0.1:8000/admin/




How to Test the Project:

Login to Django Admin:
Go to: http://127.0.0.1:8000/admin/

Add Stocks:
In Admin panel, click Stocks ➔ Add Stock.
Enter the stock name and price, then save.

Place Orders:
In Admin panel, click Orders ➔ Add Order
Choose a stock, set quantity and price, then save.

Check API Results in Browser:

http://127.0.0.1:8000/api/stocks/ to see all stocks.
http://127.0.0.1:8000/api/orders/ to see all orders.
http://127.0.0.1:8000/api/portfolio/value/ to see total portfolio value.
http://127.0.0.1:8000/api/portfolio/stock/1/ (replace 1 with your stock ID) to check investment in a stock.
