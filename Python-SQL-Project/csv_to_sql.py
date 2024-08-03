{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a771c8e1-151f-40db-b102-db2987b1aacf",
   "metadata": {},
   "source": [
    "# CSV to SQL Conversion Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d208c60a-895f-4ecb-b05d-750de7fcca5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\mahes\\anaconda3\\lib\\site-packages (2.2.2)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5c443171-a27e-4c21-840d-38bf81b49219",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mysql-connector-python in c:\\users\\mahes\\anaconda3\\lib\\site-packages (9.0.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install mysql-connector-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "908ceea9-6438-4071-914a-b035bd934bb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: matplotlib in c:\\users\\mahes\\anaconda3\\lib\\site-packages (3.8.4)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (1.4.4)\n",
      "Requirement already satisfied: numpy>=1.21 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (23.2)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (10.3.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (3.0.9)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e7c092e4-1c60-40d0-95b2-e3b501223b2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: seaborn in c:\\users\\mahes\\anaconda3\\lib\\site-packages (0.13.2)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: numpy!=1.24.0,>=1.20 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from seaborn) (1.26.4)\n",
      "Requirement already satisfied: pandas>=1.2 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from seaborn) (2.2.2)\n",
      "Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from seaborn) (3.8.4)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.4.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (23.2)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (10.3.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (3.0.9)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas>=1.2->seaborn) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from pandas>=1.2->seaborn) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\mahes\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7->matplotlib!=3.6.1,>=3.4->seaborn) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1879f767-d13a-4c5d-8118-5bab8e699081",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processing customers.csv\n",
      "NaN values before replacement:\n",
      "customer_id                 0\n",
      "customer_unique_id          0\n",
      "customer_zip_code_prefix    0\n",
      "customer_city               0\n",
      "customer_state              0\n",
      "dtype: int64\n",
      "\n",
      "Processing orders.csv\n",
      "NaN values before replacement:\n",
      "order_id                            0\n",
      "customer_id                         0\n",
      "order_status                        0\n",
      "order_purchase_timestamp            0\n",
      "order_approved_at                 160\n",
      "order_delivered_carrier_date     1783\n",
      "order_delivered_customer_date    2965\n",
      "order_estimated_delivery_date       0\n",
      "dtype: int64\n",
      "\n",
      "Processing sellers.csv\n",
      "NaN values before replacement:\n",
      "seller_id                 0\n",
      "seller_zip_code_prefix    0\n",
      "seller_city               0\n",
      "seller_state              0\n",
      "dtype: int64\n",
      "\n",
      "Processing products.csv\n",
      "NaN values before replacement:\n",
      "product_id                      0\n",
      "product category              610\n",
      "product_name_length           610\n",
      "product_description_length    610\n",
      "product_photos_qty            610\n",
      "product_weight_g                2\n",
      "product_length_cm               2\n",
      "product_height_cm               2\n",
      "product_width_cm                2\n",
      "dtype: int64\n",
      "\n",
      "Processing geolocation.csv\n",
      "NaN values before replacement:\n",
      "geolocation_zip_code_prefix    0\n",
      "geolocation_lat                0\n",
      "geolocation_lng                0\n",
      "geolocation_city               0\n",
      "geolocation_state              0\n",
      "dtype: int64\n",
      "\n",
      "Processing order_items.csv\n",
      "NaN values before replacement:\n",
      "order_id               0\n",
      "order_item_id          0\n",
      "product_id             0\n",
      "seller_id              0\n",
      "shipping_limit_date    0\n",
      "price                  0\n",
      "freight_value          0\n",
      "dtype: int64\n",
      "\n",
      "Processing payments.csv\n",
      "NaN values before replacement:\n",
      "order_id                0\n",
      "payment_sequential      0\n",
      "payment_type            0\n",
      "payment_installments    0\n",
      "payment_value           0\n",
      "dtype: int64\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import mysql.connector\n",
    "import os\n",
    "\n",
    "# List of CSV files and their corresponding table names\n",
    "csv_files = [\n",
    "    ('customers.csv', 'customers'),\n",
    "    ('orders.csv', 'orders'),\n",
    "    ('sellers.csv', 'sellers'),\n",
    "    ('products.csv', 'products'),\n",
    "    ('geolocation.csv', 'geolocation'),\n",
    "    ('order_items.csv', 'order_items'),\n",
    "    ('payments.csv', 'payments') \n",
    "]\n",
    "\n",
    "# Connect to the MySQL database\n",
    "conn = mysql.connector.connect(\n",
    "    host='localhost',\n",
    "    user='root',\n",
    "    password='Analyst@24',\n",
    "    database='ecommerce'\n",
    ")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "# Folder containing the CSV files\n",
    "folder_path = 'C:/Users/mahes/OneDrive/Desktop/Mrunal/SQL + Python Project'\n",
    "\n",
    "def get_sql_type(dtype):\n",
    "    if pd.api.types.is_integer_dtype(dtype):\n",
    "        return 'INT'\n",
    "    elif pd.api.types.is_float_dtype(dtype):\n",
    "        return 'FLOAT'\n",
    "    elif pd.api.types.is_bool_dtype(dtype):\n",
    "        return 'BOOLEAN'\n",
    "    elif pd.api.types.is_datetime64_any_dtype(dtype):\n",
    "        return 'DATETIME'\n",
    "    else:\n",
    "        return 'TEXT'\n",
    "\n",
    "for csv_file, table_name in csv_files:\n",
    "    file_path = os.path.join(folder_path, csv_file)\n",
    "    \n",
    "    # Read the CSV file into a pandas DataFrame\n",
    "    df = pd.read_csv(file_path)\n",
    "    \n",
    "    # Replace NaN with None to handle SQL NULL\n",
    "    df = df.where(pd.notnull(df), None)\n",
    "    \n",
    "    # Debugging: Check for NaN values\n",
    "    print(f\"Processing {csv_file}\")\n",
    "    print(f\"NaN values before replacement:\\n{df.isnull().sum()}\\n\")\n",
    "\n",
    "    # Clean column names\n",
    "    df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]\n",
    "\n",
    "    # Generate the CREATE TABLE statement with appropriate data types\n",
    "    columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])\n",
    "    create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'\n",
    "    cursor.execute(create_table_query)\n",
    "\n",
    "    # Insert DataFrame data into the MySQL table\n",
    "    for _, row in df.iterrows():\n",
    "        # Convert row to tuple and handle NaN/None explicitly\n",
    "        values = tuple(None if pd.isna(x) else x for x in row)\n",
    "        sql = f\"INSERT INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(row))})\"\n",
    "        cursor.execute(sql, values)\n",
    "\n",
    "    # Commit the transaction for the current CSV file\n",
    "    conn.commit()\n",
    "\n",
    "# Close the connection\n",
    "conn.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
