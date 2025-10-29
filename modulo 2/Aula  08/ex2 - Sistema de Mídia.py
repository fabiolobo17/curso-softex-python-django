class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg
    def exibir(self):
        print(f"Titulo: {self.titulo}, Duracao: {self.duracao_seg} segundos")

    def __str__(self):
        return f"{self.titulo}"

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista
    def exibir(self):
        print(f"Musica - Titulo: {self.titulo}, Duracao: {self.duracao_seg} segundos, Artista: {self.artista}")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao
    def exibir(self):
        print(f"Video - Titulo: {self.titulo}, Duracao: {self.duracao_seg} segundos, Resolucao: {self.resolucao}")

m1 = Musica("Imagine", 183, "John Lennon")
v1 = Video("Inception", 8880, "1080p")

dicionarios_midia: dict[str, list[Midia]] = {"musicas":[], "videos":[]}
dicionarios_midia["musicas"].append(m1)
dicionarios_midia["videos"].append(v1)

#print(dicionarios_midia)
for item in dicionarios_midia.values():
    for midia in item:
        midia.exibir()