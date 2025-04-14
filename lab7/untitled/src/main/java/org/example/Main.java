package org.example;

import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        // Создаем систему оповещения
        NotificationSystem notificationSystem = new NotificationSystem();

        // Добавляем посты ГАИ
        PolicePost post1 = new PolicePost("Пост ГАИ №1");
        PolicePost post2 = new PolicePost("Пост ГАИ №2");
        PolicePost post3 = new PolicePost("Пост ГАИ №3");

        notificationSystem.addObserver(post1);
        notificationSystem.addObserver(post2);
        notificationSystem.addObserver(post3);

        // Отправляем сообщение всем постам
        notificationSystem.notifyObservers("Внимание! На дороге авария. Требуется ваша помощь.");
    }
}
