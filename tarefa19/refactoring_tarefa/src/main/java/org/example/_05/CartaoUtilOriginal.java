// ... additional changes required for full refactoring
public String validar(int bandeira, String numero, String validade) {
    if (!validadeOk(validade)) {
        return CARTAO_ERRO;
    }
    String formatado = formatarNumero(numero);
    if (!formatoOk(bandeira, formatado)) {
        return CARTAO_ERRO;
    }
    if (!numeroOk(formatado)) {
        return CARTAO_ERRO;
    }
    return CARTAO_OK;
}

private boolean validadeOk(String validade) {
    // Validate the validity of the card...
}

private String formatarNumero(String numero) {
    // Format the card number...
}

private boolean formatoOk(int bandeira, String numero) {
    // Check the format of the card number...
}

private boolean numeroOk(String numero) {
    // Check the validity of the card number...
}
