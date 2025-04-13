package org.example;

public interface Observer {
    void update(String message);
}
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
