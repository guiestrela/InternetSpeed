import speedtest

test = speedtest.Speedtest()

print('Carregando lista de servidores...')
test.get_servers() # -> busta de servidores
print('Escolhendo melhor servidor....')
best = test.get_best_server() # -> escolhendo melhor servidor
print(f'Encontrado: {best["host"]} localizado em {best["country"]} ')

print('Fazendo teste de Download...')
download_result = test.download()
print('Fazendo teste de upload...')
upload_result = test.upload()
ping_result = test.results.ping

print(f'Velocidade de Download:{download_result / 1024 / 1024:.2f} Mbit/s')
print(f'Velocidade de Upload:{upload_result / 1024 / 1024:.2f} Mbit/s')
print(f'ping:{ping_result:.2f} ms')

