<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-6">
    <h1 class="text-3xl font-bold mb-6 text-blue-700">Busca de Operadoras</h1>

    <label for="busca" class="text-gray-700 mb-2 text-sm font-medium">
      Digite um termo (ex: nome da operadora, CNPJ, cidade, email, telefone, registro ANS...)
    </label>

    <div class="flex gap-2 w-full max-w-xl mb-6">
      <input
        id="busca"
        v-model="termoBusca"
        @keyup.enter="buscarOperadoras"
        placeholder="Digite algum dado conhecido"
        class="flex-grow px-4 py-2 rounded border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        @click="buscarOperadoras"
        class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
      >
        Buscar
      </button>
    </div>

    <div v-if="resultados.length" class="w-full max-w-3xl space-y-4">
      <div
        v-for="(operadora, index) in resultados"
        :key="index"
        class="bg-white p-4 rounded shadow"
      >
        <h2 class="text-lg font-semibold text-gray-800">{{ operadora.razao_social }}</h2>
        <p class="text-sm text-gray-600">CNPJ: {{ operadora.cnpj }}</p>
        <p class="text-sm text-gray-600">Cidade: {{ operadora.cidade }} - {{ operadora.uf }}</p>
        <p class="text-sm text-gray-600">CEP: {{ operadora.cep }}</p>
        <p class="text-sm text-gray-600">Email: {{ operadora.endereco_eletronico }}</p>
        <p class="text-sm text-gray-600">Telefone: {{ operadora.telefone }}</p>
        <p class="text-sm text-gray-600">Modalidade: {{ operadora.modalidade }}</p>
        <p class="text-sm text-gray-600">Registro ANS: {{ operadora.registro_ans }}</p>
      </div>
    </div>

    <p v-else class="text-gray-500 mt-4">Nenhum resultado encontrado.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const termoBusca = ref('')
const resultados = ref([])

const buscarOperadoras = async () => {
  if (!termoBusca.value.trim()) return
  try {
    const res = await fetch(`http://127.0.0.1:5000/buscar?q=${termoBusca.value}`)
    resultados.value = await res.json()
  } catch (error) {
    console.error('Erro na requisição:', error)
    resultados.value = []
  }
}
</script>
