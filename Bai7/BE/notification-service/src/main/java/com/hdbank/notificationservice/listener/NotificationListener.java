package com.hdbank.notificationservice.listener;

import com.hdbank.notificationservice.dto.OrderNotificationEvent;
import com.hdbank.notificationservice.service.NotificationService;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class NotificationListener {

    private final NotificationService notificationService;

    @KafkaListener(
            topics = "notificationTopic",
            groupId = "notification-group"
    )
    public void handleNotification(OrderNotificationEvent event) {
        notificationService.processNotification(event);
    }
}