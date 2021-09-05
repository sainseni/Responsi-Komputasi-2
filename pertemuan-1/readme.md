# Pertemuan 1 : Pengenalan Penggunaan Python

<!-- ## Tipe Data

- String
- Boolean
- Integer
- Float
- List
- Dictionary
- Tuple
- Sets

## Fungsi

- Function

## Pengkondisian

- If-else
- Loop
  - While
  - For -->

<!-- ## Struktur Data Buatan

- Arrays
- Stack
- Queue
- Trees
- Linked Lists
- Graphs
- HashMaps -->

## Tipe Data

---

### String

#### Contoh : `String`

```python
string1 = "ini nama saya"
string2 = 'yo ndak tau'
```

### Boolean

#### Contoh : `Boolean`

```python
kondisi1 = False
kondisi2 = True
```

### Integer

#### Contoh : `Integer`

```python
integer1 = 10
integer2 = 7
```

### Float

#### Contoh : `Float`

```python
float1 = 3.14
float2 = 4.20
```

### List

`List` digunakan untuk menyimpan data dari berbagai tipe data yang digabungkan menjadi satu secara terurut (beraturan dan memiliki index).

#### Contoh : `List`

```python
list1 = [1,'dua',3,'empat','5']

list2 = [1, 2, 3, 4, 5]
```

### Dictionary

`Dictionary` digunakan untuk menyimpan data berdasarkan `key-value` atau `kunci-nilai` jadi setiap nilai bisa dipanggil dengan menyebutkan kuncinya.

#### Contoh : `Dictionary`

```python
dictionary1 = {
    1 : 'list',
    2 : 'dictionary',
    3 : 'tuple',
    4 : 'sets'
}

dictionary2 = {
    'nama'      : 'udin',
    'umur'      : 19,
    'jurusan'   : 'matimatian',
    'angkatan'  : 2020
}
```

### Tuple

`Tuple` digunakan untuk menyimpan data sama halnya dengan `list` namun pada `tuple` kita tidak bisa mengubah data yang telah kita simpan (beberapa bisa namun yang lain diperlukan konversi dsb).

#### Contoh : `Tuple`

```python
tuple1 = (1, 2, 3, 4)

tuple2 = (1, 'dua', 3, 'empat')
```

### Sets

`Set` adalah himpunan item yang tidak berurutan. Elemen yang berada di dalamnya bersifat unik dan tidak dapat diduplikasi serta tidak dapat diubah.

```python
set1 = {1, 2, 3, 4, 5}

set2 = {1, "dua", "tiga", (4, 5)}
```

## Operator

---

### Penjumlahan

#### Contoh : `+`

```python
print(3+5)

# 8
```

### Pengurangan

#### Contoh : `-`

```python
print(3-5)

# -2
```

```python
print(5-3)

# 2
```

### Perkalian

#### Contoh : `*`

```python
print(3*5)

# 15
```

### Pembagian

#### Contoh : `/`

```python
print(3/5)

# 0.6
```

### Perpangkatan

#### Contoh : `**`

```python
print(3**5)

# 243
```

### Pembagian bulat

#### Contoh : `//`

```python
print(8+5)

# 1
```

### Sisa bagi

#### Contoh : `%`

```python
print(8%5)

# 3
```

---

### Fungsi

Fungsi adalah kumpulan perintah yang yang dikelompokan agar bisa dipakai kembali.

#### Contoh : `Fungsi`

```python
def function1():
  return "ini nilai"

def function2(parameter1, parameter2):
  return parameter1+parameter2
```

### Pengkondisian

### Contoh : `Pengkondisian`

```python
angka = 7

if angka >= 7:
  print('angkanya lebih dari 6')
else:
  print('angkanya kurang dari 7')
```

### For Loop

#### Contoh : `For loop`

```python
list = ['apel', 'mangga', 'nanas']

for buah in list:
  print(buah)
```

### While Loop

#### Contoh : `While loop`

```python
angka = 0

while angka <= 5:
  print('ini angka',angka)
  angka +=1
```
