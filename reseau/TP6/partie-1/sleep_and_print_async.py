import asyncio
import time

async def count_to_10():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    start_time = time.time()
    
    tasks = [ count_to_10(), count_to_10()]
    await asyncio.gather(*tasks)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Le programme a pris {elapsed_time:.2f} secondes pour s'exécuter.")
if __name__ == "__main__":
    asyncio.run(main())
