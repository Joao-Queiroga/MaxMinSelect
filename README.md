# 🚀 MaxMin Select em Python

## 📖 Descrição do projeto
Este projeto implementa o **algoritmo de seleção simultânea do maior e do menor elemento (MaxMin Select)** usando a técnica de **divisão e conquista**.

O algoritmo divide recursivamente a lista em sublistas menores, encontra o mínimo e máximo de cada sublista e combina os resultados para determinar o menor e maior elemento da lista inteira. Isso reduz o número de comparações em relação a uma abordagem ingênua, tornando o algoritmo mais eficiente.

---

## 🔎 Lógica do algoritmo
1. **Caso base 1:** se a lista tiver apenas 1 elemento, esse elemento é tanto o mínimo quanto o máximo.
2. **Caso base 2:** se a lista tiver 2 elementos, compara-os e retorna `(mínimo, máximo)`.
3. **Divisão:** a lista é dividida em duas metades.
4. **Recursão:** chama `maxmin` em cada metade.
5. **Combinação:** compara os mínimos e máximos das duas metades para obter o mínimo e máximo final.

---

## 🧩 Implementação (linha a linha)
Arquivo: `main.py`

```python
def maxmin(arr):
    # Caso base: apenas 1 elemento
    if len(arr) == 1:
        return arr[0], arr[0]

    # Caso base: 2 elementos
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    # Dividir a lista em duas metades
    mid = len(arr) // 2
    min1, max1 = maxmin(arr[:mid])
    min2, max2 = maxmin(arr[mid:])

    # Combinar os resultados
    return min(min1, min2), max(max1, max2)

# Lista de exemplo
numeros = [7, 2, 9, 4, 12, 1, 8, 10]
minimo, maximo = maxmin(numeros)
print(f"Mínimo: {minimo}, Máximo: {maximo}")
```

- `def maxmin(arr)`:
  - `if len(arr) == 1:` → retorna `(arr[0], arr[0])`.
  - `if len(arr) == 2:` → compara os dois elementos e retorna `(mín, máx)`.
  - `mid = len(arr) // 2` → divide a lista ao meio.
  - `min1, max1 = maxmin(arr[:mid])` → mínimo e máximo da primeira metade.
  - `min2, max2 = maxmin(arr[mid:])` → mínimo e máximo da segunda metade.
  - `return min(min1, min2), max(max1, max2)` → combina os resultados.

---

## ▶️ Como executar o projeto
1. Clone o repositório:
```sh
git clone https://github.com/SEU_USUARIO/maxmin_select.git
cd maxmin_select
```

2. Execute o programa:
```sh
python main.py
```

---

## 📊 Relatório Técnico

### 🔹 Complexidade Assintótica pelo método de contagem de operações
- Cada nível da recursão divide a lista em duas metades e faz **2 comparações ao combinar resultados**.
- Para `n` elementos, o número total de comparações `C(n)` segue a recorrência:
    ```
    C(n) = C(n/2) + C(n/2) + 2
    ```
- Solução aproximada: `C(n) ≈ 3n/2 - 2` comparações, menor que o método ingênuo (`2n - 2`).
- **Conclusão:** a complexidade é linear, `O(n)`.

---

### 🔹 Complexidade Assintótica pelo Teorema Mestre
- Recorrência do MaxMin Select:
```
T(n) = 2T(n/2) + O(1)
```
- Valores: `a = 2`, `b = 2`, `f(n) = O(1)`
- Calcula `log_b(a) = log_2(2) = 1`
- Caso do Teorema Mestre: **caso 2**, pois `f(n) = O(n^c)` com `c = 0 < log_b(a) = 1`
- Solução assintótica:
```
T(n) = O(n)
```
- Confirma a eficiência linear do algoritmo.

---

## 🎯 Conclusão
O MaxMin Select encontra simultaneamente o menor e maior elemento de uma lista utilizando **divisão e conquista**, com eficiência superior ao método ingênuo, percorrendo todos os elementos de forma estruturada e garantindo complexidade linear `O(n)`.
