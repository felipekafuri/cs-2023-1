import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ValidaCPFTest {
    
    @Test
    public void testCpfMaiorQue11() {
        ValidaCPF validator = new ValidaCPF();
        assertFalse(validator.isCPF("123456789012"));
    }

    @Test
    public void testCpfMenorQue3() {
        ValidaCPF validator = new ValidaCPF();
        assertFalse(validator.isCPF("12"));
    }

    @Test
    public void testCpfComLetras() {
        ValidaCPF validator = new ValidaCPF();
        assertFalse(validator.isCPF("1234567890a"));
    }

    @Test
    public void testCpfTodosNumerosIguais() {
        ValidaCPF validator = new ValidaCPF();
        assertFalse(validator.isCPF("11111111111"));
    }

    @Test
    public void testCpfValido() {
        ValidaCPF validator = new ValidaCPF();
        assertTrue(validator.isCPF("12345678909")); //CPF fictício que passa na validação
    }

    @Test
    public void testCpfInvalido() {
        ValidaCPF validator = new ValidaCPF();
        assertFalse(validator.isCPF("12345678900")); //CPF fictício que falha na validação
    }
}
