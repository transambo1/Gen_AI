package com.hdbank.order_service.service;

import com.hdbank.order_service.dto.OrderLineItemsDto;
import com.hdbank.order_service.dto.OrderRequest;
import com.hdbank.order_service.model.Order;
import com.hdbank.order_service.model.OrderLineItems;
import com.hdbank.order_service.repository.OrderRepository;
import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@Transactional
@Slf4j
public class OrderService {

    private final OrderRepository orderRepository;
    private final KafkaTemplate<String, String> kafkaTemplate;
    @CircuitBreaker(name = "inventory", fallbackMethod = "handleFallback")
    public void placeOrder(OrderRequest orderRequest) {
        Order order = new Order();
        order.setOrderNumber(UUID.randomUUID().toString());

        List<OrderLineItems> orderLineItems = orderRequest.getOrderLineItemsDtoList()
                .stream()
                .map(this::mapToDto)
                .toList();

        order.setOrderLineItemsList(orderLineItems);
        orderRepository.save(order);
        kafkaTemplate.send("notificationTopic", "Order Placed Successfully: " + order.getOrderNumber());
    }
    public void handleFallback(OrderRequest orderRequest, Throwable throwable) {
        log.error("--- CIRCUIT BREAKER KÍCH HOẠT --- Lý do: {}", throwable.getMessage());
    }
    private OrderLineItems mapToDto(OrderLineItemsDto orderLineItemsDto) {
        OrderLineItems orderLineItems = new OrderLineItems();
        orderLineItems.setPrice(orderLineItemsDto.getPrice());
        orderLineItems.setQuantity(orderLineItemsDto.getQuantity());
        orderLineItems.setSkuCode(orderLineItemsDto.getSkuCode());
        return orderLineItems;
    }
}