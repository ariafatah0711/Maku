# Additional utility functions
def transaction_to_dict(t):
    return {
        'id': t.id,
        'tanggal': t.date,
        'jenis': t.type,
        'kategori': t.category,
        'jumlah': t.amount,
        'catatan': t.note
    }
