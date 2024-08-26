import serial
 
# Configura el puerto serie
ser = serial.Serial('COM6', 9600)  # Cambia 'COM5' al puerto correcto
output_file_hcsr04 = "C:/Users/Alfonso/Desktop/Basurero/registros/registro_01.txt"

 
# Abre los archivos de salida
file_hcsr04 = open(output_file_hcsr04, "w")
 
# Lee y procesa los datos del puerto serie
while True:
    line = ser.readline().decode().strip()  # Lee una línea del puerto serie y la decodifica
    if line:
        # Separa los datos de HCSR04 y MPU6050
        data = line.split(",")
 
        # Escribe los datos en los archivos correspondientes
        file_hcsr04.write(data[0] + "\n")
 
        # Imprime los datos para verificar en la consola
        print("HCSR04:", data[0])
 
        # Flushea los archivos para asegurar que los datos se escriben correctamente
        file_hcsr04.flush()
 
# Cierra los archivos y el puerto serie al finalizar
file_hcsr04.close()
ser.close()