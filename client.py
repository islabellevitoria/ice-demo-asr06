import sys
import Ice

Ice.loadSlice('Printer.ice')
import Demo

def main():
    communicator = Ice.initialize(sys.argv)
    try:
        base = communicator.stringToProxy("SimplePrinter:tcp -h 127.0.0.1 -p 5678")
        printer = Demo.PrinterPrx.checkedCast(base)
        
        if not printer:
            raise RuntimeError("Proxy inválido para o servidor ICE")

        print("=== Testando Comunicação ZeroC ICE ===")

        res_string = printer.printString("Hello World com ICE!")
        print(f"[Cliente] Resposta de printString: {res_string}")

        meu_nome = printer.writeName()
        print(f"[Cliente] Nome retornado pelo servidor: {meu_nome}")
     
        nome_invertido = printer.reverseName(meu_nome)
        print(f"[Cliente] Nome invertido pelo servidor: {nome_invertido}")

    finally:
        communicator.destroy()

if __name__ == '__main__':
    main()
