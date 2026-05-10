<template>
  <div>
    <h2>{{ internship.title }}</h2>
    <p><strong>Company:</strong> {{ internship.company_name }}</p>
    <p><strong>Location:</strong> {{ internship.location }}</p>
    <p><strong>Duration:</strong> {{ internship.duration }}</p>
    <p><strong>Requirements:</strong></p>
    <ul>
      <li v-for="req in internship.requirements" :key="req">{{ req }}</li>
    </ul>
    <p><strong>Benefits:</strong></p>
    <ul>
      <li v-for="ben in internship.benefits" :key="ben">{{ ben }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import internshipApi from '../api/internship'

const internship = ref({})

onMounted(async () => {
  const { data } = await internshipApi.getInternship(route.params.id)
  internship.value = data
})

import { useRoute } from 'vue-router'
const route = useRoute()
</script>
