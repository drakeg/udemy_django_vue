Vue.component("comment", {
    props: {
        comment: {
            type: Object,
            required: true,
        }
    },
    template: `
        <div>
            <div class="card-body">
                <p>{{ comment.username }}</p>
                <p>{{ comment.content }}</p>
            </div>
        </div>
    `
})

var app = new Vue({
    el: '#app',
    data: {
       comments: [
           { username: "alice", content: "first comment!" },
           { username: "bob", content: "bob's comment!" },
           { username: "jesus", content: "this is the 10th comment!" },
       ]
    },
    computed: {
       
    },
    methods: {

    }
})