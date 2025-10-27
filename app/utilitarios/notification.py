class Notification:
    def __init__(self):
        self.notifications: list = []

    def add_notification(self,text: str) -> None:
        self.notifications.append(text)
    
    def has_notification(self) -> bool:
        return len(self.notifications) > 0
    
    def get_notification(self) -> list:
        return self.notifications
    
    def clear_notification(self) -> None:
        self.notifications.clear() 
