using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Collections.Generic;
using DotnetClient.Models;

namespace DotnetClient.Services
{
    public interface ITaskService
    {
        Task<List<TaskDto>> ListTasksAsync();
        Task<TaskDto> GetTaskByIdAsync(string id);
        Task<TaskDto> CreateTaskAsync(string title, string description);
        Task<TaskDto> UpdateTaskAsync(string id, object updateData);
        Task DeleteTaskAsync(string id);
    }

    public class TaskService : ITaskService
    {
        private readonly HttpClient _httpClient;
        private readonly string _baseUrl = "http://localhost:5000/api/tasks";

        public TaskService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<List<TaskDto>> ListTasksAsync()
        {
            var response = await _httpClient.GetStringAsync(_baseUrl);
            return JsonConvert.DeserializeObject<List<TaskDto>>(response);
        }

        public async Task<TaskDto> GetTaskByIdAsync(string id)
        {
            var response = await _httpClient.GetStringAsync($"{_baseUrl}/{id}");
            return JsonConvert.DeserializeObject<TaskDto>(response);
        }

        public async Task<TaskDto> CreateTaskAsync(string title, string description)
        {
            var taskData = new { title, description };
            return await PostAsync<TaskDto>(_baseUrl, taskData);
        }

        public async Task<TaskDto> UpdateTaskAsync(string id, object updateData)
        {
            return await PutAsync<TaskDto>($"{_baseUrl}/{id}", updateData);
        }

        public async Task DeleteTaskAsync(string id)
        {
            var response = await _httpClient.DeleteAsync($"{_baseUrl}/{id}");
            response.EnsureSuccessStatusCode();
        }

        private async Task<T> PostAsync<T>(string url, object data)
        {
            var json = JsonConvert.SerializeObject(data);
            var content = new StringContent(json, System.Text.Encoding.UTF8, "application/json");
            
            var response = await _httpClient.PostAsync(url, content);
            response.EnsureSuccessStatusCode();
            
            var responseBody = await response.Content.ReadAsStringAsync();
            return JsonConvert.DeserializeObject<T>(responseBody);
        }

        private async Task<T> PutAsync<T>(string url, object data)
        {
            var json = JsonConvert.SerializeObject(data);
            var content = new StringContent(json, System.Text.Encoding.UTF8, "application/json");
            
            var response = await _httpClient.PutAsync(url, content);
            response.EnsureSuccessStatusCode();
            
            var responseBody = await response.Content.ReadAsStringAsync();
            return JsonConvert.DeserializeObject<T>(responseBody);
        }
    }
}