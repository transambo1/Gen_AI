package com.hdbank.notificationservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NotificationController {

    @GetMapping("/api/notification/test")
    public String test() {
        return "Notification Service is running";
    }
}