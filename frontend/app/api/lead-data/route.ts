import { NextResponse } from 'next/server';
import { readFile } from 'fs/promises';
import { join } from 'path';

export async function GET() {
  try {
    // Try to read lead_data.json from backend directory
    const filePath = join(process.cwd(), '..', 'backend', 'lead_data.json');
    const fileContent = await readFile(filePath, 'utf-8');
    const data = JSON.parse(fileContent);
    
    return NextResponse.json(data);
  } catch (error) {
    // File doesn't exist yet or can't be read
    return NextResponse.json({}, { status: 404 });
  }
}
