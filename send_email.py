import datetime
import logging

logging.basicConfig(filename='notifications.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(message):
    print(f"Отправка email: {message}")
    logging.info(f"Email отправлен: {message}")

def send_sms(message):
    print(f"Отправка SMS: {message}")
    logging.info(f"SMS отправлено: {message}")

def send_notification(notification_type, callback, message):
    try:
        if notification_type == "email":
            callback(message)
        elif notification_type == "sms":
            callback(message)
        else:
            raise ValueError("Unknown notification type")
    except ValueError as e:
       print(f"Ошибка: {e}")
       logging.error(f"Ошибка отправки уведомления: {e}")

if __name__ == "__main__":
    send_notification("email", send_email, "Привет, это тестовое письмо!")
    send_notification("sms", send_sms, "Привет, это тестовое SMS!")
    send_notification("push", send_sms, "Привет, это push!")
    send_notification("email", send_email, "Еще одно тестовое письмо")