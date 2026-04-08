package com.hdbank.notificationservice.service;

import com.hdbank.notificationservice.dto.OrderNotificationEvent;
import org.springframework.stereotype.Service;

@Service
public class NotificationService {

    public void processNotification(OrderNotificationEvent event) {
        System.out.println("======================================");
        System.out.println("📩 Received notification");
        System.out.println("Order Number: " + event.getOrderNumber());
        System.out.println("Message: " + event.getMessage());
        System.out.println("📧 Simulating confirmation email for order: " + event.getOrderNumber());
        System.out.println("======================================");
    }
}