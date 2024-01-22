AWS de Validação de EPI
Descrição
Este projeto implementa um sistema de detecção de Equipamentos de Proteção Individual (EPI) utilizando a Amazon Rekognition. Ele utiliza uma câmera para capturar imagens de indivíduos e analisar, em tempo real, se estão usando EPIs apropriados, como máscaras faciais e luvas, com base na inteligência artificial e no aprendizado de máquina fornecidos pela AWS.

Tecnologias Utilizadas
Python
OpenCV (cv2)
Amazon Rekognition
Amazon Boto3
Funcionamento
O código usa a biblioteca OpenCV para capturar imagens de uma câmera conectada. Cada frame capturado é analisado para detectar a presença de pessoas utilizando a detecção de corpos do Haar Cascade do OpenCV. Em seguida, o sistema verifica, utilizando a Amazon Rekognition, se as pessoas detectadas estão usando os EPIs necessários. As imagens das pessoas sem EPI são salvas em uma pasta especificada para revisão posterior.

Instalação e Configuração
Para instalar e configurar este projeto, siga os passos abaixo:

Clone o repositório para sua máquina local.
Instale as dependências necessárias (OpenCV, Boto3).
Configure suas credenciais da AWS (Access Key ID e Secret Access Key) no script.
Certifique-se de ter uma webcam ou câmera conectada ao seu computador.
Uso
Para usar este sistema, execute o script Python. Ele iniciará a captura de vídeo da câmera conectada e começará a análise de EPI em tempo real. Para encerrar a execução, pressione 'q'.

AWS License
Para usar este projeto, você precisará de uma licença AWS válida, pois ele faz uso do serviço AWS Rekognition.

Contribuições
Contribuições são bem-vindas! Para contribuir, por favor, siga estas etapas:

Faça um fork do repositório.
Crie uma nova branch para suas mudanças.
Faça suas alterações.
Envie um pull request.


Contato
Para quaisquer dúvidas ou sugestões, por favor entre em contato através de Breno.mine@gmail.com .
