"""Salva e apaga fotos de itens. Valida pelo conteúdo do arquivo, não pelo nome."""
import uuid
from pathlib import Path

MAX_BYTES = 5 * 1024 * 1024


def _extension(head):
    if head.startswith(b'\xff\xd8\xff'):
        return '.jpg'
    if head.startswith(b'\x89PNG\r\n\x1a\n'):
        return '.png'
    if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
        return '.webp'
    return None


def save_item_image(file, folder):
    """Devolve o nome do arquivo salvo, ou None se nenhum arquivo foi enviado.

    Levanta ValueError se a foto for grande demais ou não for JPG, PNG ou WebP.
    """
    if file is None or not file.filename:
        return None

    data = file.stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('A foto passa de 5 MB.')

    extension = _extension(data[:12])
    if extension is None:
        raise ValueError('Envie a foto em JPG, PNG ou WebP.')

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    name = uuid.uuid4().hex + extension
    (folder / name).write_bytes(data)
    return name


def delete_item_image(name, folder):
    if not name:
        return
    path = Path(folder) / Path(name).name  # Path(name).name impede sair da pasta
    if path.is_file():
        path.unlink()