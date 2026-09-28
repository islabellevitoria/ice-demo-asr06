import sys
import Ice

Ice.loadSlice('Printer.ice')
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(f"[Servidor] printString recebido: {s}")
        return s + "*"

    # new methods
    def writeName(self, current=None):
        nome = "Islabelle"
        print(f"[Servidor] writeName chamado. Retornando: {nome}")
        return nome

    def reverseName(self, s, current=None):
        nome_invertido = s[::-1]
        print(f"[Servidor] reverseName recebido: '{s}' -> Invertido: '{nome_invertido}'")
        return nome_invertido

def main():
    communicator = Ice.initialize(sys.argv)
    try:
        adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
        servant = PrinterI()
        adapter.add(servant, Ice.Identity("SimplePrinter"))
        adapter.activate()
        print("Servidor ZeroC ICE rodando na porta 5678...")
        communicator.waitForShutdown()
    finally:
        communicator.destroy()

if __name__ == '__main__':
    main()
