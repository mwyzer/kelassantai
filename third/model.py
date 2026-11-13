
# model.py
# ==================================================
# MODEL — Class Siswa
# ==================================================

class Siswa:
    """Cetakan (class) untuk membuat object siswa."""

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def status(self):
        if self.nilai >= 75:
            return f"{self.nama} LULUS (nilai {self.nilai})"

        return f"{self.nama} belum lulus (nilai {self.nilai})"

    def to_dict(self):
        """Mengubah object menjadi dictionary."""
        return {
            "nama": self.nama,
            "nilai": self.nilai
        }

    @classmethod
    def from_dict(cls, data):
        """Mengubah dictionary menjadi object Siswa."""
        return cls(
            data["nama"],
            data["nilai"]
        )


class SiswaBerprestasi(Siswa):
    """Class turunan dari Siswa."""

    def status(self):
        return f"{self.nama} JUARA! (nilai {self.nilai})"
