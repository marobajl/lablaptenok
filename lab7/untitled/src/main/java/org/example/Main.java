package org.example;

import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(String message);
}

// Конкретный наблюдатель: Пост ГАИ
class PolicePost implements Observer {
    private String postName;

    public PolicePost(String postName) {
        this.postName = postName;
    }

    @Override
    public void update(String message) {
        System.out.println(postName + " получил сообщение: " + message);
    }
}

interface Subject {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers(String message);
}


class NotificationSystem implements Subject {
    private List<Observer> observers;

    public NotificationSystem() {
        observers = new ArrayList<>();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
}

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
