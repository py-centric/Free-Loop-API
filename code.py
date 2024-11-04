from datetime import datetime
import requests
import json

url = "https://cb-public-api-f5dovyimaq-ew.a.run.app/orders/create"

api_key = ""
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

payload = {
    "branch_id": "h1H6WKLwkjTctAYry6yB",
    "order": {
        "order_no": "16",
        "alcohol": True,
        "assignable": True,
        "customer": {"name": "Test Customer", "mobile_no": "+27830000000"},
        "address": "21 Junction Ave, Parktown, Johannesburg",
        "location": {"latitude": -26.042088, "longitude": 28.016763},
        "collection_time": "2022-10-07T10:00:00+02:00",
        "delivery_time": "2022-10-07T15:20:00+02:00",
        "contact_person": {
            "name": "Olivia Kunis",
            "role": "Packer",
            "mobile_no": "+27781234567",
        },
        "instructions": "Call on delivery",
        "delivery_price": 90,
        "payment_type": "cash",
        "origination": "app",
        "parcels": [{"qr_code": "ESTIMATE1", "size": "Small"}],
        "abandon_flow": {"type": "sog"},
        "delivery_flow": {"type": "otp", "code": "1234"},
    },
}


def create_order(url, headers, payload):
    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            print("Single order created successfully:", response.json())
        else:
            print(f"Failed to create order. Status code: {response.status_code}")
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def create_orders(url, headers, payload):
    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            print("Multiple orders created successfully:", response.json())
        else:
            print(f"Failed to create orders. Status code: {response.status_code}")
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def get_order(url, headers, order_id):
    try:
        response = requests.get(f"{url}/{order_id}", headers=headers)
        if response.status_code == 200:
            print("Order retrieved successfully:", response.json())
        else:
            print(f"Failed to retrieve order. Status code: {response.status_code}")
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def get_orders(url, headers, order_ids):
    try:
        query_params = {"order_ids": json.dumps(order_ids)}
        response = requests.get(url, headers=headers, params=query_params)
        if response.status_code == 200:
            print("Orders retrieved successfully:", response.json())
        else:
            print(f"Failed to retrieve orders. Status code: {response.status_code}")
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def cancel_order(url, headers, order_id):
    try:
        cancel_url = f"{url}/{order_id}/cancel"
        response = requests.delete(cancel_url, headers=headers)
        if response.status_code == 200:
            print("Order canceled successfully:", response.json())
        else:
            print(f"Failed to cancel order. Status code: {response.status_code}")
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def schedule_delivery_time(url, headers, order_id, delivery_time):
    try:
        schedule_url = f"{url}/{order_id}/schedule/delivery-time"
        payload = {"order": {"delivery_time": delivery_time}}
        response = requests.put(schedule_url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Delivery time scheduled successfully:", response.json())
        else:
            print(
                f"Failed to schedule delivery time. Status code: {response.status_code}"
            )
            print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
