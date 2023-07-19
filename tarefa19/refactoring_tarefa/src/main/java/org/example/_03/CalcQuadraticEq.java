package org.example._03;

public class CalcQuadraticEq {
    public double[] calcQuadraticEq(double a, double b, double c) {
        double D = b * b - 4 * a * c;
        if (D > 0) {
            double sqrtD = Math.sqrt(D);
            double x1 = (-b - sqrtD) / (2 * a);
            double x2 = (-b + sqrtD) / (2 * a);
            return new double[]{x1, x2};
        } else if (D == 0) {
            double x = -b / (2 * a);
            return new double[]{x};
        } else {
            return new double[]{}; // No roots
        }
    }
}
