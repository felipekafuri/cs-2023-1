package org.example._02;

class Human {
    private String name;
    private int age;  // Change to int type
    private String country;
    private String city;
    private String street;
    private String house;
    private String quarter;

    // Getters and setters would be needed for these attributes...

    public String getFullAddress() {
        return String.format("%s, %s, %s, %s %s", country, city, street, house, quarter);
    }
}
