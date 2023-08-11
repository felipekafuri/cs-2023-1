package org.example._04;


// classe salary é redundante pode ser removida
public class Employee {
    private double salary;
    private double awards;

    public double getYearlySalary(){
        return salary*12;
    }

    public double getAwards(){
        return awards;
    }

    public double getMonthlySalary() {
        return (getYearlySalary() + getAwards())/12;
    }
}
