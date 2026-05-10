<template>
  <div>
    <h2>Internship Listings</h2>
    <ul>
      <li v-for="post in internships" :key="post.id">
        <router-link :to="{ name: 'InternshipDetail', params: { id: post.id } }">
          {{ post.title }} - {{ post.company_name }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import internshipApi from '../api/internship'

const internships = ref([])

onMounted(async () => {
  const { data } = await internshipApi.getInternships()
  internships.value = data
})
</script>
