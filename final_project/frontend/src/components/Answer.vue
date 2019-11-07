<template>
<div class="single-answer">
    <p class="text-muted">
        <strong>{{ answer.author }}</strong> &#8901; {{ answer.created_at }}
        <p>{{ answer.body }}</p>
        <hr>
    </p>
</div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        }
    }
}
</script>