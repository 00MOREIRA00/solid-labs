from abc import ABC, abstractmethod


# 1️⃣ ISP + DIP - Criamos interfaces específicas para reduzir acoplamento
class PedidoInterface(ABC):
    @abstractmethod
    def processar(self):
        pass

class NotificacaoInterface(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


# 2️⃣ LSP - Podemos trocar os tipos de pratos sem quebrar o código

class PedidoComida(PedidoInterface): 
    def processar(self):
        return 'Pedido de comida processado'
    
class PedidoBebida(PedidoInterface):
    def processar(self):
        return 'Pedido de bebida processado'
    

# 3️⃣ OCP - Criamos novas notificações sem modificar o código existente

class NotificacaoEmail(NotificacaoInterface):
    def enviar(self, mensagem):
        print(f"📧 Enviando email: {mensagem}")

class NotificacaoSMS(NotificacaoInterface):
    def enviar(self, mensagem):
        print(f"📱 Enviando SMS: {mensagem}")


# 4️⃣ SRP - Gerencia os pedidos (única responsabilidade)

class GerenciadorDePedidos:
    def __init__(self, pedido: PedidoInterface, notificacao: NotificacaoInterface):
        self.pedido = pedido
        self.notificacao = notificacao
    
    def executar(self): 
        mensagem = self.pedido.processar()
        self.notificacao.enviar(mensagem)

# 5️⃣ Testando a aplicação

pedido_comida = PedidoComida()
pedido_bebida = PedidoBebida()

notificacao_email = NotificacaoEmail()
notificacao_sms = NotificacaoSMS()

gerenciador1 = GerenciadorDePedidos(pedido_comida, notificacao_email)
gerenciador1.executar()

gerenciador2 = GerenciadorDePedidos(pedido_bebida, notificacao_sms)
gerenciador2.executar()

        