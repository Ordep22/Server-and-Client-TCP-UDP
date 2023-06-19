try {

SERIAL1.getInstance().escreverComando("Abrindo Socket de Comunicao!");

SERIAL1.getInstance().escreverComando(Prints.separador());

if (this.protocolo == 0) {

socketRoteamento = (SocketConnection) Connector.open(this.paremetrosConexao);
inputStream = socketRoteamento.openInputStream();
outPutStream = socketRoteamento.openOutputStream();

}

else {

DatagramConnection connection = (DatagramConnection) Connector.open("datagram://" + getHost() + ":"
+ getPortaTCP(), Connector.READ_WRITE, true);

while (sendDgram == true) {

// System.out.println("Criando uma datagram com 1000 bytes");

datagram = connection.newDatagram(1000);

// System.out.println("[info] Enviando a mensagem");

// Esse msg deve ser algo que est vindo pala serial
// do equipamento
// Por equanto isso et sendo simulado por uma
// varivel local
sendDatagram(connection, datagram, msgTosend);

if (sendDgram == true) {

datagram = connection.newDatagram(1000);

// Aqui quero saber qual  a resposta do servidor

msg = receiveDatagram(connection, datagram);
SERIAL1.getInstance().escreverComando("[info] Mensagem recebida do servidor:" + msg);
// System.out.println("sendDgram == True");

} else {
// System.out.println("sendDgram == Fause");
break;

}

}

}
