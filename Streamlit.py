import streamlit as st
import qrcode

def generate_qr_code(url):
    # Cria um objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Adiciona os dados (URL) ao QRCode
    qr.add_data(url)
    qr.make(fit=True)

    # Cria uma imagem PIL a partir do QRCode
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.title("Gerador de QR Code")

    # Obtém a URL do usuário
    url = st.text_input("Digite a URL para gerar o QR Code:")

    if st.button("Gerar QR Code"):
        if url:
            # Gera o QR Code
            qr_code = generate_qr_code(url)

            # Exibe o QR Code na interface
            st.image(qr_code, caption="QR Code gerado", use_column_width=True)
        else:
            st.warning("Por favor, digite uma URL válida.")

if __name__ == "__main__":
    main()