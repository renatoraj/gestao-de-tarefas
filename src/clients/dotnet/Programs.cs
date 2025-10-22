using System;
using System.Net.Http;
using System.Threading.Tasks;
using DotnetClient.Services;
using DotnetClient.Models;  // ⭐ ADICIONAR ESTE USING

namespace DotnetClient
{
    class Program
    {
        private static readonly ITaskService _taskService = 
            new TaskService(new HttpClient());

        static async Task Main(string[] args)
        {
            Console.WriteLine("=== Client .NET - API de Gerenciamento de Tarefas ===");
            Console.WriteLine("Conectando à API Python em: http://localhost:5000");
            Console.WriteLine();
            
            try
            {
                await ShowMenu();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Erro crítico: {ex.Message}");
            }
            
            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
        
        static async Task ShowMenu()
        {
            while (true)
            {
                Console.WriteLine("\n=== MENU PRINCIPAL ===");
                Console.WriteLine("1. Listar todas as tarefas");
                Console.WriteLine("2. Criar nova tarefa");
                Console.WriteLine("3. Buscar tarefa por ID");
                Console.WriteLine("4. Atualizar tarefa");
                Console.WriteLine("5. Deletar tarefa");
                Console.WriteLine("0. Sair");
                Console.Write("Escolha uma opção: ");
                
                var option = Console.ReadLine();
                Console.WriteLine();
                
                try
                {
                    switch (option)
                    {
                        case "1":
                            await ListTasks();
                            break;
                        case "2":
                            await CreateTaskInteractive();
                            break;
                        case "3":
                            await GetTaskById();
                            break;
                        case "4":
                            await UpdateTaskInteractive();
                            break;
                        case "5":
                            await DeleteTaskInteractive();
                            break;
                        case "0":
                            Console.WriteLine("Saindo...");
                            return;
                        default:
                            Console.WriteLine("Opção inválida! Tente novamente.");
                            break;
                    }
                }
                catch (HttpRequestException ex)
                {
                    Console.WriteLine($"❌ Erro de conexão: {ex.Message}");
                    Console.WriteLine("Verifique se a API Python está rodando na porta 5000");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"❌ Erro: {ex.Message}");
                }
            }
        }
        
        static async Task ListTasks()
        {
            Console.WriteLine("📋 Buscando tarefas...");
            var tasks = await _taskService.ListTasksAsync();
            
            if (tasks == null || tasks.Count == 0)
            {
                Console.WriteLine("Nenhuma tarefa encontrada.");
                return;
            }
            
            Console.WriteLine($"\n=== TAREFAS ENCONTRADAS ({tasks.Count}) ===");
            foreach (var task in tasks)
            {
                PrintTask(task);
                Console.WriteLine("---");
            }
        }
        
        static async Task CreateTaskInteractive()
        {
            Console.WriteLine("➕ Criando nova tarefa");
            Console.Write("Título: ");
            var title = Console.ReadLine();
            
            if (string.IsNullOrWhiteSpace(title))
            {
                Console.WriteLine("❌ Título é obrigatório!");
                return;
            }
            
            Console.Write("Descrição (opcional): ");
            var description = Console.ReadLine();
            
            try
            {
                var newTask = await _taskService.CreateTaskAsync(title, description ?? "");
                Console.WriteLine($"✅ Tarefa criada com sucesso!");
                PrintTask(newTask);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Erro ao criar tarefa: {ex.Message}");
            }
        }
        
        static async Task GetTaskById()
        {
            Console.Write("🔍 ID da tarefa: ");
            var id = Console.ReadLine();
            
            if (string.IsNullOrWhiteSpace(id))
            {
                Console.WriteLine("❌ ID é obrigatório!");
                return;
            }
            
            try
            {
                var task = await _taskService.GetTaskByIdAsync(id);
                Console.WriteLine($"\n=== TAREFA ENCONTRADA ===");
                PrintTask(task);
            }
            catch (HttpRequestException ex) when (ex.Message.Contains("404"))
            {
                Console.WriteLine("❌ Tarefa não encontrada!");
            }
        }
        
        static async Task UpdateTaskInteractive()
        {
            Console.Write("✏️ ID da tarefa para atualizar: ");
            var id = Console.ReadLine();
            
            if (string.IsNullOrWhiteSpace(id))
            {
                Console.WriteLine("❌ ID é obrigatório!");
                return;
            }
            
            // Primeiro busca a tarefa atual
            TaskDto currentTask;
            try
            {
                currentTask = await _taskService.GetTaskByIdAsync(id);
            }
            catch
            {
                Console.WriteLine("❌ Tarefa não encontrada!");
                return;
            }
            
            Console.WriteLine($"Tarefa atual: {currentTask.Title}");
            Console.WriteLine("Deixe em branco para manter o valor atual");
            
            Console.Write($"Novo título [{currentTask.Title}]: ");
            var newTitle = Console.ReadLine();
            
            Console.Write($"Nova descrição [{currentTask.Description}]: ");
            var newDescription = Console.ReadLine();
            
            Console.Write($"Concluída (s/n) [{(currentTask.IsComplete ? "s" : "n")}]: ");
            var completedInput = Console.ReadLine();
            
            var updateData = new
            {
                title = string.IsNullOrWhiteSpace(newTitle) ? null : newTitle,
                description = string.IsNullOrWhiteSpace(newDescription) ? null : newDescription,
                is_complete = string.IsNullOrWhiteSpace(completedInput) ? 
                    null : (bool?)(completedInput.ToLower() == "s")
            };
            
            try
            {
                var updatedTask = await _taskService.UpdateTaskAsync(id, updateData);
                Console.WriteLine("✅ Tarefa atualizada com sucesso!");
                PrintTask(updatedTask);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Erro ao atualizar tarefa: {ex.Message}");
            }
        }
        
        static async Task DeleteTaskInteractive()
        {
            Console.Write("🗑️ ID da tarefa para deletar: ");
            var id = Console.ReadLine();
            
            if (string.IsNullOrWhiteSpace(id))
            {
                Console.WriteLine("❌ ID é obrigatório!");
                return;
            }
            
            Console.Write("Tem certeza? (s/n): ");
            var confirmation = Console.ReadLine();
            
            if (confirmation?.ToLower() != "s")
            {
                Console.WriteLine("Operação cancelada.");
                return;
            }
            
            try
            {
                await _taskService.DeleteTaskAsync(id);
                Console.WriteLine("✅ Tarefa deletada com sucesso!");
            }
            catch (HttpRequestException ex) when (ex.Message.Contains("404"))
            {
                Console.WriteLine("❌ Tarefa não encontrada!");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Erro ao deletar tarefa: {ex.Message}");
            }
        }
        
        static void PrintTask(TaskDto task)
        {
            Console.WriteLine($"ID: {task.Id}");
            Console.WriteLine($"Título: {task.Title}");
            Console.WriteLine($"Descrição: {task.Description ?? "(sem descrição)"}");
            Console.WriteLine($"Status: {(task.IsComplete ? "✅ Concluída" : "⏳ Pendente")}");
            Console.WriteLine($"Criada em: {task.CreatedAt:dd/MM/yyyy HH:mm}");
        }
    }
}