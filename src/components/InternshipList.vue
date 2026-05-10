<template>
  <div>
    <h1>Internship List</h1>
    <ul>
      <li v-for="internship in internships" :key="internship.id">
        {{ internship.title }} - {{ internship.company }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchInternships } from '../api/internship'

const internships = ref([])

onMounted(async () => {
  try {
    const { data } = await fetchInternships()
    internships.value = data
  } catch (err) {
    console.error(err)
  }
})
</script>
