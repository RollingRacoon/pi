"""Salva e apaga fotos de itens. Valida pelo conteúdo do arquivo, não pelo nome."""
import uuid
from pathlib import Path

# Tamanho máximo de cada foto: 5 MB.
MAX_BYTES = 5 * 1024 * 1024


def _extension(head):
    # Descobre o tipo real da imagem pelos primeiros bytes do arquivo
    # ("assinatura"), sem confiar na extensão que o usuário mandou.
    if head.startswith(b'\xff\xd8\xff'):
        return '.jpg'
    if head.startswith(b'\x89PNG\r\n\x1a\n'):
        return '.png'
    if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
        return '.webp'
    return None  # formato não aceito


def save_item_image(file, folder):
    """Devolve o nome do arquivo salvo, ou None se nenhum arquivo foi enviado.

    Levanta ValueError se a foto for grande demais ou não for JPG, PNG ou WebP.
    """
    # Foto é opcional: sem arquivo, não há o que salvar.
    if file is None or not file.filename:
        return None

    # Lê um byte a mais que o limite só para saber se passou dele.
    data = file.stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('A foto passa de 5 MB.')

    extension = _extension(data[:12])
    if extension is None:
        raise ValueError('Envie a foto em JPG, PNG ou WebP.')

    # Cria a pasta se necessário e salva com nome aleatório (uuid),
    # evitando nomes repetidos e nomes maliciosos vindos do usuário.
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    name = uuid.uuid4().hex + extension
    (folder / name).write_bytes(data)
    return name


def delete_item_image(name, folder):
    # Apaga a foto do disco (usado ao trocar a foto ou se o cadastro falhar).
    if not name:
        return
    path = Path(folder) / Path(name).name  # Path(name).name impede sair da pasta
    if path.is_file():
        path.unlink()